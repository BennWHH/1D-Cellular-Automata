import CellControls
import JSONControls

while True:

    print("\nOptions")
    print("1: Save new rule")
    print("2: Load current rules")
    print("3: Retrieve specific rule")
    print("4: Use specific rule")
    selection = input("Select an option (1-4): ")
    if selection.isdigit():
        selection = int(selection)
    else:
        continue

    if selection == 1:
        ruleNumber, ruleArray = JSONControls.generateRuleArray()
        JSONControls.saveRulesArray(ruleNumber, ruleArray)
    elif selection == 2:
        print(JSONControls.loadRuleArray())
    elif selection == 3:
        ruleNumber = int(input("Which rule? "))
        JSONControls.getRuleArray(ruleNumber)
    elif selection == 4:
        generations = int(input("How many generations? "))
        ruleNumber = int(input("Which rule? "))
        rule = JSONControls.getRuleArray(ruleNumber)
        cellSelection = input("Select cell states: ")
        currentCellStates = [int(bit) for bit in cellSelection]
        print(currentCellStates)
        if not all(i in {'0', '1'} for i in cellSelection):
            print("Invalid array")
            continue
        else:
            CellControls.newGeneration(rule, currentCellStates, generations)
    else:
        print("Invalid option.")