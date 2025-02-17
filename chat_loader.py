def load_chat_context():
  try:
      with open("chat.txt", "r", encoding='utf-8') as f:
          chat_content = f.read()
          messages = []
          for line in chat_content.split('\n'):
              if line.strip():
                  if line.startswith("User:"):
                      messages.append({
                          "parts": [{"text": line[5:].strip()}],
                          "role": "user"
                      })
                  elif line.startswith("Assistant:"):
                      messages.append({
                          "parts": [{"text": line[10:].strip()}],
                          "role": "model"
                      })
                  else:
                      continue
          return messages
  except FileNotFoundError:
      print("chat.txt not found. Starting with empty context.")
      return []
  except Exception as e:
      print(f"Error loading chat context: {e}")
      return []