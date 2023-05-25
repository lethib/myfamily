import { useQuery } from "@tanstack/react-query";

import { GetFamilyResponse } from "../types/api";

import { familyApiInstance as api } from "./api";

export const useGetFamilyQuery = (path: string) =>
  useQuery<GetFamilyResponse>(["families"], () =>
    api.get<GetFamilyResponse>(path)
  );
