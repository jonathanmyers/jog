package main

import (
	"embed"
	"log"
	"net/http"
)

//go:embed static/*
var content embed.FS

func main() {
	fs := http.FileServer(http.FS(content))
	http.Handle("/", fs)

	log.Print("Listening on :8080...")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatal(err)
	}
}
