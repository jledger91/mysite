import { LOGGED_IN, LOGGED_OUT } from './actions';

export const initialState = {
  firstName: undefined,
  lastName: undefined,
  username: undefined,
}

const authReducer = function (state = initialState, action) {
  switch (action.type) {
    case LOGGED_IN:
      return {
        ...state,
        firstName: action.payload.firstName,
        lastName: action.payload.lastName,
        username: action.payload.username,
      }
    case LOGGED_OUT:
      return initialState;
    default:
      return state;
  }
}

export default authReducer;
