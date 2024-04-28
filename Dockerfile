FROM golang:1.22.2-bookworm
EXPOSE 4000
WORKDIR /app


COPY . /app
# компилируем go file
RUN go build ./main.go 
# запускаем сервер на go
CMD ["./main"]

