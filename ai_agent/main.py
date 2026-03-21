from agent import create_agent

def main():
    agent = create_agent()
    
    while True:
        query = input("\nEnter Your Task(type 'exit' to quit):")
        
        if query.lower() == 'exit':
            break
        
        response = agent.run(query)
        
        print("\nFinal Output")
        print(response)
        
if __name__ == "__main__":
    main()