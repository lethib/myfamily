import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { Tree } from "react-d3-tree";
import { Box } from "@mui/material";
import { ThemeProvider } from "@mui/material/styles";

import { theme } from "./themes/typography";
import { useRect } from "./hooks/useRect";

import { FamilyCard } from "./components/familyCard";
import { tempTreeData } from "./data/tempTreeData";

function App() {
  const client = new QueryClient();
  const [treeRect, treeRef] = useRect();
  return (
    <QueryClientProvider client={client}>
      <ThemeProvider theme={theme}>
        <Box width="100vw" height="100vh" ref={treeRef}>
          <Tree
            data={tempTreeData}
            renderCustomNodeElement={(props) => <FamilyCard {...props} />}
            orientation="vertical"
            dimensions={
              treeRect
                ? { height: treeRect.height, width: treeRect.width }
                : undefined
            }
            nodeSize={{ x: 500, y: 300 }}
          />
        </Box>
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;
