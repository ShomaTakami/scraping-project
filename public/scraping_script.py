import requests
import time
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # 追加
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  # ここでKeysを追加
# ブラウザのドライバーを選択（例: Chrome）
driver = webdriver.Chrome()

# ログイン情報
login_form = {
    # 'utf-8': '✓',
    # 'authenticity_token': 'token',
    'user[login_code]': 'takatoshi.ayabe@dreamexchange.onmicrosoft.com',
    'user[password]': 'ABC123!!!',
    # 'commit': 'ログイン'
}

# ログイン
login_url = 'https://base.next-engine.org/users/sign_in'
driver.get(login_url)

# # ログインフォームに情報を入力
# for field, value in login_form.items():
#     element = driver.find_element_by_name(field)
#     element.send_keys(value)

# # ログインボタンをクリック
# driver.find_element_by_name('commit').click()
# # セッションの作成
# session = requests.Session()
# # ログイン情報
# login_form = {
#     'utf-8':'✓',
#     'authenticity_token':'token',
#     'user[login_code]': 'takatoshi.ayabe@dreamexchange.onmicrosoft.com',
#     'user[password]': 'ABC123!!!',
#     'commit': 'ログイン'
# }
# # ログイン
# login_url = 'https://base.next-engine.org/users/sign_in'
# def get_authenticity_token(session, login_url):
#     response = session.get(login_url)
#     response.encoding = response.apparent_encoding
#     bs = BeautifulSoup(response.text, 'html.parser')
#     authenticity_token = str(bs.find(attrs={'name':'authenticity_token'}).get('value'))
#     return authenticity_token
# if __name__ == '__main__':
#     session = requests.Session()
#     authenticity_token = get_authenticity_token(session, login_url)
#     login_form['authenticity_token'] = authenticity_token
# login_response = session.post(login_url, data=login_form)
# ログイン成功かどうかの確認
# if 'ログインしました' in login_response.text:
# 		# print('Login success.')
# 		# TOPページからリンクを取得
# 		# top_page_url = 'https://base.next-engine.org/'
# 		top_page_url = 'https://google.com/'
# 		top_page_response = session.get(top_page_url)
# 		# BeautifulSoupでHTMLを解析
# 		# top_page_soup = BeautifulSoup(top_page_response.text, 'html.parser')
# 		# # リンク先のURLを取得
# 		# target_link = top_page_soup.find('a', {'data-analytics-name': 'footer_app_execution'})
# 		# target_link_url = urljoin(top_page_url, target_link['href'])
# 		# # リンク先に移動
# 		# target_link_response = session.get(target_link_url)
# 		# # BeautifulSoupでHTMLを解析
# 		# soup = BeautifulSoup(target_link_response.text, 'html.parser')
# 		# # <h1> タグのテキストを取得して表示
# 		# title_text = soup.find('title').get_text()
# 	  # TOPページからリンクを取得
# 		target_page_url = 'https://main.next-engine.com/Userjyuchumeisai'
# 		# ヘッドレスモードを有効にする
# 		options = Options()
# 		options.add_argument('--headless')
# 		# ブラウザのドライバーを選択（例: Chrome）
# 		driver = webdriver.Chrome()
# 		# driver = webdriver.Chrome(options=options)
# 		# 対象のWebページにアクセス
# 		driver.get(top_page_url)
# 		driver.get(target_page_url)
# 		# try:
# 		# 		# ボタンがクリック可能になるまで待機 (10秒でタイムアウト)
# 		# 		button = WebDriverWait(driver, 10).until(
# 		# 				EC.element_to_be_clickable((By.ID, 'jyuchu_dlg_open'))
# 		# 		)
# 		# 		# ボタンをクリック
# 		# 		button.click()
# 		# 		print('click')
# 		# 		# ここで検索画面が開いた後の処理を追加
# 		# 		# 日付ピッカーの要素を取得
# 		# 		datepicker_from = driver.find_element(By.ID, 'sea_jyuchu_search_field03_from')
# 		# 		datepicker_to = driver.find_element(By.ID, 'sea_jyuchu_search_field03_to')
# 		# 		# 期間を指定したい日付を設定
# 		# 		start_date = '2023/01/08'
# 		# 		end_date = '2023/01/09'
# 		# 		# 日付ピッカーに日付を入力
# 		# 		datepicker_from.clear()
# 		# 		datepicker_from.send_keys(start_date)
# 		# 		datepicker_to.clear()
# 		# 		datepicker_to.send_keys(end_date)
# 		# 		# Enterキーを押して確定（もしくはピッカーが自動的に閉じるような処理）
# 		# 		datepicker_to.send_keys(Keys.ENTER)
# 		# 						# ボタンがクリック可能になるまで待機 (10秒でタイムアウト)
# 		# 		search_button = WebDriverWait(driver, 10).until(
# 		# 				EC.element_to_be_clickable((By.ID, 'ne_dlg_btn2_searchJyuchuDlg'))
# 		# 		)
# 		# 		# ボタンをクリック
# 		# 		search_button.click()

# 		# 		# downloaded_file_name = 'downloaded_file.csv'
# 		# 		# downloaded_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), downloaded_file_name)
# 		# 		# # 検索結果をCSVでダウンロードするリンクのID
# 		# 		# download_link_id = 'searchJyuchu_table_dl_lnk'
# 		# 		# # ダウンロードリンクがクリック可能になるまで待機 (10秒でタイムアウト)
# 		# 		# download_link = WebDriverWait(driver, 10).until(
# 		# 		# 		EC.element_to_be_clickable((By.ID, download_link_id))
# 		# 		# )
# 		# 		# # ダウンロードリンクをクリック
# 		# 		# download_link.click()
# 		# 		# # ダウンロードが完了するまで待機 (ここでは簡略化して5秒待機)
# 		# 		# time.sleep(5)
# 		# 		# # ファイルが保存されたことを確認
# 		# 		# if os.path.exists(downloaded_file_path):
# 		# 		# 		print(f"CSVファイルが保存されました: {downloaded_file_path}")
# 		# 		# else:
# 		# 		# 		print("ファイルが保存されませんでした。")
# 		# finally:
# 		# 		driver.quit()
# else:
# 		print('Login failed.')
