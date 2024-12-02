'use client'
import React, { useState } from "react";
import { useServerInsertedHTML } from "next/navigation";
import { ServerStyleSheet, StyleSheetManager } from "styled-components";

// Assuming `isPropValid` is defined somewhere
const isPropValid = (propName: string) => true;

interface StyledComponentsRegistryProps {
  children: React.ReactNode;
  props?: Record<string, unknown>; // Adjust the type as needed
}

export default function StyledComponentsRegistry({
  children,
  props,
}: StyledComponentsRegistryProps) {
  const [styledComponentsStyleSheet] = useState(() => new ServerStyleSheet());

  useServerInsertedHTML(() => {
    const styles = styledComponentsStyleSheet.getStyleElement();
    styledComponentsStyleSheet.instance.clearTag();
    return <>{styles}</>;
  });

  if (typeof window !== "undefined") return <>{children}</>;

  return (
    <StyleSheetManager
      enableVendorPrefixes
      shouldForwardProp={(propName, elementToBeRendered) => {
        return typeof elementToBeRendered === "string"
          ? isPropValid(propName)
          : true;
      }}
      {...(props || {})}
      sheet={styledComponentsStyleSheet.instance}
    >
        {children}
    </StyleSheetManager>
  );
}