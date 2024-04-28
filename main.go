package main
 
import (
"net/http"
"html/template"
"path/filepath"
)
 
func main() {
http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
startPage(w)
})
http.ListenAndServe(":4000", nil)
}



func startPage(rw http.ResponseWriter) {
	//указываем путь к нужному файлу
	path := filepath.Join("public", "index.html")
	//создаем html-шаблон
	tmpl, err := template.ParseFiles(path)
	if err != nil {
		http.Error(rw, err.Error(), 400)
		return
	}
	//выводим шаблон клиенту в браузер
	err = tmpl.Execute(rw, nil)
	if err != nil {
		http.Error(rw, err.Error(), 400)
		return
	}
}
