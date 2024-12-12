import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const circuitApi = createApi({
  reducerPath: "circuitApi",
  baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:5000'}),
  endpoints: (builder) => ({
    // Existing endpoints
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

    // Additional endpoints
    bellStateCircuit: builder.query({
      query: () => ({
        url: "/bellStateCircuit",
        method: "GET",
      }),
    }),
    basicGatesCircuit: builder.query({
      query: () => ({
        url: "/basicGatesCircuit",
        method: "GET",
      }),
    }),
    qftCircuit: builder.query({
      query: () => ({
        url: "/qftCircuit",
        method: "GET",
      }),
    }),
    teleportationCircuit: builder.query({
      query: () => ({
        url: "/teleportationCircuit",
        method: "GET",
      }),
    }),
    vqeCircuit: builder.query({
      query: () => ({
        url: "/vqeCircuit",
        method: "GET",
      }),
    }),
    phaseEstimationCircuit: builder.query({
      query: () => ({
        url: "/phaseEstimationCircuit",
        method: "GET",
      }),
    }),
    deutschJozsaCircuit: builder.query({
      query: () => ({
        url: "/deutschJozsaCircuit",
        method: "GET",
      }),
    }),
    entanglementSwappingCircuit: builder.query({
      query: () => ({
        url: "/entanglementSwappingCircuit",
        method: "GET",
      }),
    }),
    circuitInfo: builder.query({
      query: (circuit_name) => ({
        url: `/info/${circuit_name}`,
        method: "GET",
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
  useBellStateCircuitQuery,  // New hooks for additional endpoints
  useBasicGatesCircuitQuery,
  useQftCircuitQuery,
  useTeleportationCircuitQuery,
  useVqeCircuitQuery,
  usePhaseEstimationCircuitQuery,
  useDeutschJozsaCircuitQuery,
  useEntanglementSwappingCircuitQuery,
  useCircuitInfoQuery,
  useLazyHadamardGateQuery,
  useLazyPauliYGateQuery,
  useLazyPauliZGateQuery,
  useLazyPhaseGateQuery,
  useLazyTGateQuery,
  useLazyXGateQuery,
} = circuitApi;
