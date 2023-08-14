
import requests
import tkinter as tk
from tkinter import scrolledtext
import webbrowser
class GoogleSearch:
    def __init__(self, api_key, cse_id):
        self.api_key = api_key
        self.cse_id = cse_id

    def search(self, query, num_results=10):
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={self.api_key}&cx={self.cse_id}&num={num_results}"

        response = requests.get(url)
        results = response.json()

        if 'items' not in results:
            return []

        search_results = []
        for item in results['items']:
            link = item['link']
            if self._is_site_accessible(link):  # Добавим проверку на доступность перед добавлением результатов
                search_results.append({
                    'title': item['title'],
                    'link': link
                })

        return search_results

    def _is_site_accessible(self, url):
        try:
            response = requests.head(url, timeout=5)
            return 200 <= response.status_code < 400
        except requests.RequestException:
            return False


class SearchGUI:
    def __init__(self, search_engine):
        self.search_engine = search_engine

        self.window = tk.Tk()
        self.window.title("Google Search GUI")

        self.query_entry = tk.Entry(self.window, width=50)
        self.query_entry.pack(pady=10)

        self.search_button = tk.Button(self.window, text="Search", command=self.perform_search)
        self.search_button.pack(pady=10)

        self.results_area = tk.Text(self.window, wrap=tk.WORD, width=70, height=10)
        self.results_area.pack(pady=10)
        self.results_area.tag_config("hyper", foreground="blue", underline=True)
        self.results_area.tag_bind("hyper", "<Button-1>", self.open_link)

    def perform_search(self):
        query = self.query_entry.get()
        results = self.search_engine.search(query, num_results=5)

        self.results_area.delete(1.0, tk.END)  # очищаем область результатов
        for result in results:
            self.results_area.insert(tk.END, result['title'] + '\n')
            self.results_area.insert(tk.END, result['link'] + '\n', ("hyper",))
            self.results_area.insert(tk.END, '---' + '\n')

    def open_link(self, event):
        link_index = self.results_area.index(tk.CURRENT)
        line_num, col_num = map(int, link_index.split("."))
        link = self.results_area.get(f"{line_num}.0", f"{line_num}.end")
        webbrowser.open(link.strip())

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    API_KEY = 'AIzaSyAjiPiaHQ8lPXV0zgGC1nVHTCCSiUTMRIc'
    CSE_ID = '07dfef113cccc44f7'

    google = GoogleSearch(API_KEY, CSE_ID)
    gui = SearchGUI(google)
    gui.run()
