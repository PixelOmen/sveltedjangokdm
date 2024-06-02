import { writable } from "svelte/store";

const token = localStorage.getItem("token");
export const isAuthenticated = writable(!!token);

export function save_token(token: string) {
  localStorage.setItem("token", token);
  isAuthenticated.set(true);
}

export function remove_token() {
  localStorage.removeItem("token");
  isAuthenticated.set(false);
}

export function get_token() {
  return localStorage.getItem("token");
}