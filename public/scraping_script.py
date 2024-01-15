import requests
import time
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta

options = Options()
# 実際の挙動を確認したい場合は↓をコメントアウト
options.add_argument('--headless')
# ダウンロードフォルダの指定
# TODO 本番環境時に修正 本番パス->/var/www/html/storage/app/uploads
downloaddir = '/home/shoma/keymetron/scraping-project/database/next-csv'
options.add_experimental_option("prefs", {"download.default_directory": downloaddir})
# ブラウザのドライバーを選択（Chrome）
driver = webdriver.Chrome(options = options)
# ログイン情報
login_form = {
    # 'utf-8':'✓',
    # 'authenticity_token':'token',
    'user[login_code]': 'takatoshi.ayabe@dreamexchange.onmicrosoft.com',
    'user[password]': 'ABC123!!!',
    # 'commit': 'ログイン'
}
# ログイン
login_url = 'https://base.next-engine.org/users/sign_in'
driver.get(login_url)
# ログインフォームに情報を入力
for field, value in login_form.items():
    element = driver.find_element(By.NAME, field)
    element.send_keys(value)
# ログインボタンをクリック
commit_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-large.span12')  # CSSセレクタを使用
commit_button.click()

top_page_url = 'https://base.next-engine.org/'
driver.get(top_page_url)
top_page_source = driver.page_source
top_page_soup = BeautifulSoup(top_page_source, 'html.parser')
target_link = top_page_soup.find('a', {'data-analytics-name': 'footer_app_execution'})
target_link_url = urljoin(top_page_url, target_link['href'])
# リンク先に移動
driver.get(target_link_url)
# 管理画面へ
target_page_url = 'https://main.next-engine.com/Userjyuchumeisai'
driver.get(target_page_url)
# 検索モーダルを開くボタンがクリック
search_button = driver.find_element(By.ID, 'jyuchu_dlg_open')
search_button.click()
# ここで検索画面が開いた後の処理を追加
# 日付ピッカーの要素を取得
datepicker_from = driver.find_element(By.ID, 'sea_jyuchu_search_field03_from')
datepicker_to = driver.find_element(By.ID, 'sea_jyuchu_search_field03_to')
# 期間を指定したい日付を設定
# 日付ピッカーに日付を入力（現在は前日を指定）
today_date_obj = datetime.now()
today_date_str = today_date_obj.strftime('%Y/%m/%d')
previous_day_date_obj = today_date_obj - timedelta(days=1)
previous_day_date_str = previous_day_date_obj.strftime('%Y/%m/%d')
start_date = previous_day_date_str
datepicker_from.clear()
datepicker_from.send_keys(start_date)
end_date = previous_day_date_str
datepicker_to.clear()
datepicker_to.send_keys(end_date)
# Enterキーを押して確定（もしくはピッカーが自動的に閉じるような処理）
datepicker_to.send_keys(Keys.ENTER)
# 検索ボタンがクリック
search_action_button = driver.find_element(By.ID, 'ne_dlg_btn2_searchJyuchuDlg')
search_action_button.click()
# 検索結果の表示を待つ
time.sleep(2)
# ダウンロードリンクをクリック
download_link = driver.find_element(By.ID, 'searchJyuchu_table_dl_lnk')
download_link.click()
# ここで適切な待機時間（秒）を指定
time.sleep(10)
# ブラウザを閉じる
driver.quit()
