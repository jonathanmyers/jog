package main

import (
	"embed"
	"io/fs"
	"log"
	"net/http"
)

//go:embed static/*
var content embed.FS

func main() {
	serverRoot, err := fs.Sub(content, "static")
	if err != nil {
		log.Fatal(err)
	}

	fs := http.FileServer(http.FS(serverRoot))
	http.Handle("/", fs)

	log.Print("Listening on :8080...")
	err = http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatal(err)
	}
}
