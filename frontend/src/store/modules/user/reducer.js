import { LOGGED_OUT, SET_USER } from './actions';

export const initialState = {
  firstName: undefined,
  lastName: undefined,
  username: undefined,
}

const userReducer = function (state = initialState, action) {
  switch (action.type) {
    case LOGGED_OUT:
      return initialState;
    case SET_USER:
      return {
        ...state,
        firstName: action.payload.firstName,
        lastName: action.payload.lastName,
        username: action.payload.username,
      }
    default:
      return state;
  }
}

export default userReducer;
