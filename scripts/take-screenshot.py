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

        # Wait for the main content (including the map) to become visible
        await page.wait_for_selector('#main-content', state='visible')

        # Add a small delay for map tiles to load
        await page.wait_for_timeout(2000)

        # Take a screenshot of the entire page
        await page.screenshot(path=args.output, full_page=True)

        await browser.close()
        print(f"Screenshot saved to {args.output}")

if __name__ == '__main__':
    asyncio.run(main())
