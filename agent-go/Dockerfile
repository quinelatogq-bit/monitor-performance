# Estágio 1: Build
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY . .
RUN go build -o agente main.go

# Estágio 2: Execução (Imagem final fica com apenas ~15MB)
FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/agente .
CMD ["./agente"]
