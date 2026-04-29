FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY . .
RUN go build -o agente main.go

FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/agente .
# Instalando o tzdata para o agente ter a hora correta se precisar
RUN apk add --no-cache tzdata
CMD ["./agente"]
