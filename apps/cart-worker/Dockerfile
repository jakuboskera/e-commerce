FROM golang:1.23-alpine AS builder

WORKDIR /build

COPY go.mod .
COPY main.go .

RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o app .

FROM scratch

COPY --from=builder /build/app /app

EXPOSE 8080

ENTRYPOINT ["/app"]
