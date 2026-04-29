package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"runtime"
	"time"
)

type Stats struct {
	CPU     int    `json:"cpu"`
	RAM     uint64 `json:"ram"`
	OS      string `json:"os"`
	Threads int    `json:"threads"`
}

func main() {
	url := "http://server:5000/report"
	fmt.Println("🚀 Agente de Monitoramento iniciado no Debian 12...")

	for {
		var m runtime.MemStats
		runtime.ReadMemStats(&m)

		payload := Stats{
			CPU:     runtime.NumCPU(),
			RAM:     m.Alloc / 1024 / 1024, // Em MB
			OS:      runtime.GOOS,
			Threads: runtime.NumGoroutine(),
		}

		jsonData, _ := json.Marshal(payload)
		resp, err := http.Post(url, "application/json", bytes.NewBuffer(jsonData))

		if err != nil {
			fmt.Printf("❌ Erro ao enviar dados: %v\n", err)
		} else {
			fmt.Printf("✅ Dados enviados: %d MB RAM em uso | Status: %s\n", payload.RAM, resp.Status)
			resp.Body.Close()
		}

		time.Sleep(2 * time.Second) // Intervalo de coleta
	}
}
