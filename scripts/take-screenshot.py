import asyncio
from playwright.async_api import async_playwright
import os
import argparse

async def main():
    parser = argparse.ArgumentParser(description='Take a screenshot of the trip timeline.')
    parser.add_argument('--output', default='timeline.png', help='Output file path for the screenshot.')
    args = parser.parse_args()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Go to the local server
        await page.goto('http://localhost:8000/index.html')

        # Wait for the city timeline to be rendered
        await page.wait_for_selector('#city-timeline-container .city-timeline')

        # Take a screenshot of the city timeline container
        element_handle = await page.query_selector('#city-timeline-container')
        await element_handle.screenshot(path=args.output)

        await browser.close()
        print(f"Screenshot saved to {args.output}")

if __name__ == '__main__':
    asyncio.run(main())
