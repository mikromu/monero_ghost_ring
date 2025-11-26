import requests, time

def ghost_ring():
    print("Monero — The Ghost Ring Just Signed Its Name in the Fog")
    seen = set()
    while True:
        r = requests.get("https://xmrscan.com/api/recent")
        for tx in r.json().get("data", []):
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)

            # Monero hides everything, but ring size 16+ with huge input count = someone is hiding a fortune
            inputs = tx.get("inputs", 0)
            ring = tx.get("ring_size", 11)
            amount = tx.get("amount", 0) / 1e12

            if inputs > 200 and ring >= 16 and amount > 5000:  # >5000 XMR moved with extreme obfuscation
                print(f"THE GHOST RING SPOKE\n"
                      f"{amount:,.0f} XMR vanished into perfect darkness\n"
                      f"Inputs: {inputs} — more shadows than stars\n"
                      f"Ring size: {ring} — mathematically untraceable\n"
                      f"Hash: {h[:16]}...\n"
                      f"Block: {tx['height']}\n"
                      f"https://xmrscan.com/tx/{h}\n"
                      f"→ Someone just signed their name in invisible ink\n"
                      f"→ Not even the fog remembers where it went\n"
                      f"→ This is privacy made religion.\n"
                      f"{'◈ ▩ ◈ ▩'*25}\n")
        time.sleep(4.2)

if __name__ == "__main__":
    ghost_ring()
