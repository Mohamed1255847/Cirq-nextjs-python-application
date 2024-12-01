import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const circuitApi = createApi({
  reducerPath: "circuitApi",
  baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:5000'}),
  endpoints: (builder) => ({
    setupCircuit: builder.mutation({
      query: () => ({
        url: "/setup-circuit",
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      }),
    }),
    runCircuit: builder.mutation({
      query: () => ({
        url: "/run-cirq",
        method: "POST",
      }),
    }),
    hadamardGate: builder.query({
      query: () => ({
        url: "/hadamardGate",
        method: "GET",
      }),
    }),
    xGate: builder.query({
      query: () => ({
        url: "/xGate",
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }),
    }),
    pauliYGate: builder.query({
      query: () => ({
        url: "/pauliYGate",
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }),
    }),
    pauliZGate: builder.query({
      query: () => ({
        url: "/pauliZGate",
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }),
    }),
    phaseGate: builder.query({
      query: () => ({
        url: "/phaseGate",
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }),
    }),
    tGate: builder.query({
      query: () => ({
        url: "/tGate",
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }),
    }),
  }),
});

export const {
  useSetupCircuitMutation,
  useRunCircuitMutation,
  useHadamardGateQuery,
  useXGateQuery,
  usePauliYGateQuery,
  usePauliZGateQuery,
  usePhaseGateQuery,
  useTGateQuery,
  useLazyHadamardGateQuery,
  useLazyPauliYGateQuery,
  useLazyPauliZGateQuery,
  useLazyPhaseGateQuery,
  useLazyTGateQuery,
  useLazyXGateQuery,
} = circuitApi;
