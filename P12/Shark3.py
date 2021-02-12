class Shark:

    animal_type = 'fish'
    location = 'ocean'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_followers(self, followers):
        self.followers = followers
        print('This user has ' + str(followers))

def main():

    sammy = Shark('Sammy', 5)

    print(sammy.name)

    print(sammy.location

    stephan = Shark('Stephan', 8)

    print(stephan.name)
    stephan.set_followers(77)
    print(stephan.animal_type)

    # Exercise

    jessica = Shark('Jessica', 4)
    jessica.set_followers(87)
    print(jessica.animal_type)
    print(jessica.location)

if __name__ == '__main__':
    main()