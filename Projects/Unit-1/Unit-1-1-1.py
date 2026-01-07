from dotenv import load_dotenv
from Projects.llm import get_llm


def main():
    load_dotenv()

    llm = get_llm()
    #res = llm.invoke("Reply with exactly: OK")
    #print(res.content)

    


if __name__ == "__main__":
    main()
