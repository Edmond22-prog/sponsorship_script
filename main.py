import json

from datetime import datetime

from core.sponsoring_process import SponsoringProcess
from utils.getters_utils import retrieve_godfathers, retrieve_godsons


def main():
    VALIDATED_GODFATHERS, REVOKED_GODFATHERS = retrieve_godfathers("godfathers_2023_2024.csv")
    VALIDATED_GODSONS, REVOKED_GODSONS = retrieve_godsons("godsons_2023_2024.csv")
    
    print(f"Total number of godfathers: {len(VALIDATED_GODFATHERS)+len(REVOKED_GODFATHERS)}")
    print(f"Validated godfathers: {len(VALIDATED_GODFATHERS)}")
    print(f"Revoked godfathers: {len(REVOKED_GODFATHERS)}")
    print("================================================================================")
    print(f"Total number of godsons: {len(VALIDATED_GODSONS)+len(REVOKED_GODSONS)}")
    print(f"Validated godsons: {len(VALIDATED_GODSONS)}")
    print(f"Revoked godsons: {len(REVOKED_GODSONS)}")
    print("================================================================================")
    print(f"Min godson by godfather: {len(VALIDATED_GODSONS) // len(VALIDATED_GODFATHERS)}\n")
    
    sponsoring_process = SponsoringProcess(VALIDATED_GODFATHERS, VALIDATED_GODSONS)
    sponsoring_process.execution()
    sponsoring_process.display_sponsorship()
    
    # This part is for the generation of the JSON list who will be use by the Frontend
    SPONSORSHIPS = sponsoring_process.get_sponsorship()
    SPONSORSHIPS_JSON = [sponsorship.toJSON() for sponsorship in SPONSORSHIPS]
    # Sort the list by the godfather's name
    SPONSORSHIPS_JSON.sort(key=lambda value:value["godfather"]["name"])
    # Build the json file
    with open(f"sponsorships_{datetime.now().timestamp()}.json", "w") as file:
        json.dump(SPONSORSHIPS_JSON, file, indent=4, ensure_ascii=False)


if "__main__" == __name__:
    main()
