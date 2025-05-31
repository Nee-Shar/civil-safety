# run_all.py
import asyncio
import subprocess

async def run_uvicorn():
    proc = await asyncio.create_subprocess_exec(
        "uvicorn", "main:app", "--reload"
    )
    await proc.wait()

async def run_bot():
    proc = await asyncio.create_subprocess_exec("python", "telegram-bot.py")
    await proc.wait()

async def main():
    await asyncio.gather(run_uvicorn(), run_bot())

asyncio.run(main())
