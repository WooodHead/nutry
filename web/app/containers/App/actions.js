import {
  DEFAULT_ACTION,
  LOGIN_CLICKED,
  LOGIN_SUCCESS,
  LOGIN_FAILURE,
} from './constants';

export function defaultAction() {
  return {
    type: DEFAULT_ACTION,
  };
}
export function login() {
  return {
    type: LOGIN_CLICKED,
  };
}
export function loginSuccess(token) {
  return {
    type: LOGIN_SUCCESS,
    token,
  };
}
export function loginFailure(err) {
  return {
    type: LOGIN_FAILURE,
    err,
  };
}