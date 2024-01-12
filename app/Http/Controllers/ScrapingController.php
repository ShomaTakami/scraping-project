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
        if ($exitCode === 0) {
            $result = is_string($output) ? json_decode($output, true) : $output;

            return response()->json(['data' => $result]);
        } else {
            dd("Error executing Python script. Exit code: {$exitCode}", $output); // エラー時の処理
        }
    }
}
