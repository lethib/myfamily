import { Family, Person, FamilyPerson } from "../models";

export type CompleteFamily = Family & { persons: Person[] & { family_relations: FamilyPerson[] } }


export interface GetFamilyResponse {
  family: CompleteFamily;
}
