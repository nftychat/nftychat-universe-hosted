import React from "react";
import ReactDOM from "react-dom/client";
import { UniversalDm, UniversalSupport } from "nftychat-universe";

const dm_div = document.getElementById("nfty_universal_dm");
if (!dm_div) {
  const dm_root = ReactDOM.createRoot(dm_div);
  dm_root.render(
    <React.StrictMode>
      <UniversalDm
        address={dm_div.dataset.address}
        displayName={dm_div.dataset.display_name}
        theme={dm_div.dataset.theme}
      />
    </React.StrictMode>
  );
}

const support_div = document.getElementById("nfty_universal_support");
if (support_div) {
  const support_root = ReactDOM.createRoot(support_div);
  support_root.render(
    <React.StrictMode>
      <UniversalSupport
        address={support_div.dataset.address}
        chatTitle={support_div.dataset.chat_title}
        welcomeMessage={support_div.dataset.welcome_message}
        theme={support_div.dataset.theme}
      />
    </React.StrictMode>
  );
}
