from pet import Pet

def main():
    # Create a pet
    my_pet = Pet("Fluffy")
    
    # Initial status
    my_pet.get_status()
    
    # Test methods
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.get_status()
    
    # Train some tricks
    my_pet.train("sit")
    my_pet.train("roll over")
    my_pet.train("play dead")
    
    # Show tricks
    my_pet.show_tricks()
    
    # Final status
    my_pet.get_status()

if __name__ == "__main__":
    main()