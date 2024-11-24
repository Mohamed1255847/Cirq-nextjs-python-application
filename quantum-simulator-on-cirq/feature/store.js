import { configureStore } from "@reduxjs/toolkit";
import { circuitApi } from "./api";
import { setupListeners } from "@reduxjs/toolkit/query";

export const store = configureStore({
  reducer: {
    [circuitApi.reducerPath]: circuitApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(circuitApi.middleware),
});
setupListeners(store.dispatch);
