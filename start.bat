@echo  off

call %~dp0shop_bot\venv\Scripts\activate

cd %~dp0shop_bot

python tel_bot.py 

pause