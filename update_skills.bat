@echo off
echo =========================================
echo Nuwa Skills Data Sync
echo =========================================
echo.
echo 正在掃描並打包所有 SKILL.md 到網頁資料庫...
node build_data.js
if %errorlevel% neq 0 (
    echo.
    echo ❌ 打包失敗，請檢查 Node.js 是否正確安裝。
    pause
    exit /b %errorlevel%
)
echo.
echo ✅ 打包完成！請重新整理網頁載入最新角色。
pause
