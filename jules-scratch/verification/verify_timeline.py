from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Go to the local server
        page.goto('http://localhost:8000')

        # Wait for the loading overlay to be hidden
        page.wait_for_selector('#loading-overlay.hidden')

        # Wait for animations to complete
        page.wait_for_timeout(1000)

        # Take a screenshot of the timeline
        timeline_element = page.query_selector('#city-timeline-container')
        if timeline_element:
            timeline_element.screenshot(path="jules-scratch/verification/timeline_verification.png")

        browser.close()

if __name__ == "__main__":
    run()
