from splinter.browser import Browser                   # importeer de Browser klasse
browser = Browser('chrome')                            # instantieer een browser object
browser.visit("https://duckduckgo.com")                # laat de browser naar een URL navigeren
browser.fill('q', 'raspberry pi retro website')        # vul een zoektekst in
button = browser.find_by_id('search_button_homepage')  # Zoek de Zoek knop
button.click()                                         # Druk op de knop
browser.quit()                                         # Sluit de browser