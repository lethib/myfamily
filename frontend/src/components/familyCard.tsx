import { Paper, Typography } from "@mui/material";
import { CustomNodeElementProps } from "react-d3-tree";
import { useTheme } from "@mui/material/styles";

import { useRect } from "../hooks/useRect";

export const FamilyCard = ({
  nodeDatum,
  toggleNode,
}: CustomNodeElementProps) => {
  const theme = useTheme();
  const [cardRect, cardRef] = useRect();
  const relation = "P";
  return (
    <foreignObject
      width="20%"
      height="10%"
      x={cardRect ? -cardRect.width / 2 : 0}
      y={cardRect ? -cardRect.height / 2 : 0}
      onClick={toggleNode}
    >
      <Paper sx={{ height: "100%" }} ref={cardRef}>
        <Typography color={theme.palette.success.main}>
          {nodeDatum.name}
        </Typography>
        <Typography>{relation}</Typography>
      </Paper>
    </foreignObject>
  );
};
