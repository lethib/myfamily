import { RawNodeDatum } from "react-d3-tree";

export const tempTreeData: RawNodeDatum = {
    name: "Famille Ancienne",
    children: [
      {
        name: "Enfant 1",
        attributes: {
          relation: "C",
        },
        children: [
          {
            name: "test",
          },
        ],
      },
      {
        name: "Enfant 2",
      },
    ],
  };