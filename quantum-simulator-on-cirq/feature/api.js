import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const circuitApi = createApi({
  reducerPath: 'circuitApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:5000' }),
  endpoints: (builder) => ({
    setupCircuit: builder.mutation({
      query: () => ({
        url: '/setup-circuit',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      }),
    }),
    runCircuit: builder.mutation({
      query: () => ({
        url: '/run-cirq',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      }),
    }),
  }),
});

export const { useSetupCircuitMutation, useRunCircuitMutation } = circuitApi;
