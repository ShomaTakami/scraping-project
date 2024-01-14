<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

class ScrapingController extends Controller
{
    public function index()
    {
        return view('scraping.index');
    }

    public function scrapeData()
    {
        $pythonScriptPath = public_path('scraping_script.py');
        $command = "python3 {$pythonScriptPath} 2>&1"; // 2>&1 は標準エラー出力も含めて取得するための記述
        exec($command, $output, $exitCode);

        if ($exitCode == 0) {
            // スクリプト実行成功時の処理
            // ダウンロードフォルダの指定
            $downloadDir = public_path('../database/next-csv');
            // ダウンロードフォルダ内の一番上のファイルを取得
            // ダウンロードフォルダ内の一番上のファイルを取得
            $files = scandir($downloadDir);
            $latestFile = $files[2]; // カレントディレクトリと親ディレクトリを除くためのインデックス2
            // 今日の年月日を取得
            $todayDate = date('Ymd');
            // ファイル名を年月日に変更
            $newFileName = "{$todayDate}.csv";
            $newFilePath = "{$downloadDir}/{$newFileName}";
            // ファイル名変更
            rename("{$downloadDir}/{$latestFile}", $newFilePath);

            return response()->json(['message' => 'Success']);
        } else {
            return response()->json(['message' => 'False']);
        }
    }
}
