import random
import json


def generateRuleArray():
    ruleNumber = random.randint(0, 255)
    ruleBinary = f"{ruleNumber:08b}"
    ruleArray = [int(bit) for bit in ruleBinary]
    return ruleNumber, ruleArray

def saveRulesArray(ruleNumber, ruleArray):
    try:
        with open("Rules.json", "r") as file:
            rules = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        rules = {}

    if str(ruleNumber) in rules:
        print(f"Rule {ruleNumber} already exists. Skipping save.")
        return

    rules[str(ruleNumber)] = ruleArray

    with open("Rules.json", "w") as file:
        json.dump(rules, file, indent=4)
    print(f"Rule {ruleNumber} saved successfully")

def loadRuleArray():
    try:
        with open("Rules.json", "r") as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return {}

def getRuleArray(ruleNumber):
    try:
        with open("Rules.json", "r") as file:
            rules = json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        print("Rules file not found")
        return

    ruleArray = rules.get(str(ruleNumber))
    if ruleArray is not None:
        print(f"Rule {ruleNumber}: {ruleArray}")
        return ruleArray
    else:
        print(f"Rule {ruleNumber} not found.")
        return None
