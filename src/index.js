import React from "react";
import ReactDOM from "react-dom/client";
import {UniversalDm} from 'nftychat-universe'

const div = document.getElementById("nfty_universal_dm");
const root = ReactDOM.createRoot(div);
root.render(
  <React.StrictMode>
    <UniversalDm
      address={div.dataset.address}
      displayName={div.dataset.display_name}
      theme={div.dataset.theme}
    />
  </React.StrictMode>
);
