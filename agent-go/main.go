package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"os/signal"
	"runtime"
	"syscall"
	"time"
)

type Stats struct {
	CPU     int    `json:"cpu"`
	RAM     uint64 `json:"ram"`
	Threads int    `json:"threads"`
	System  string `json:"system"`
}

func main() {
	// Pega a URL do servidor via variável de ambiente ou usa default
	url := os.Getenv("SERVER_URL")
	if url == "" {
		url = "http://localhost:5000/report"
	}

	// Canal para capturar o sinal de interrupção (Ctrl+C ou Docker stop)
	stop := make(chan os.Signal, 1)
	signal.Notify(stop, os.Interrupt, syscall.SIGTERM)

	fmt.Printf("🚀 Monitor iniciado. Reportando para: %s\n", url)

	// Loop em uma Goroutine para não travar o sinal de stop
	go func() {
		for {
			var m runtime.MemStats
			runtime.ReadMemStats(&m)

			data := Stats{
				CPU:     runtime.NumCPU(),
				RAM:     m.Alloc / 1024 / 1024,
				Threads: runtime.NumGoroutine(),
				System:  runtime.GOOS,
			}

			sendData(url, data)
			time.Sleep(3 * time.Second)
		}
	}()

	<-stop // O programa "trava" aqui até você mandar parar
	fmt.Println("\n👋 Encerrando agente de forma segura...")
}

func sendData(url string, data Stats) {
	jsonData, _ := json.Marshal(data)
	
	// Client com Timeout (Sênior não usa o DefaultClient sem timeout!)
	client := &http.Client{Timeout: 2 * time.Second}
	
	resp, err := client.Post(url, "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Printf("⚠️  Servidor offline. Tentando novamente em breve...\n")
		return
	}
	defer resp.Body.Close()
	fmt.Printf("📊 Métricas enviadas: %d MB RAM em uso.\n", data.RAM)
}
