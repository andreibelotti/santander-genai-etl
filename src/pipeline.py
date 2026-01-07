from extract import extract_user_ids, extract_user_data
from transform import generate_marketing_message
from load import load_news

def run_pipeline():
    user_ids = extract_user_ids("data/SDW2023.csv")

    for user_id in user_ids:
        user = extract_user_data(user_id)
        if not user:
            continue

        message = generate_marketing_message(user)
        success = load_news(user, message)

        if success:
            print(f"Usuário {user['name']} atualizado com sucesso")
        else:
            print(f"Falha ao atualizar usuário {user_id}")

if __name__ == "__main__":
    run_pipeline()
