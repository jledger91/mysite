import {
  CLEAR_USER,
  SET_USER,
  SET_USERS,
} from './actions';

export const initialState = {
  detail: undefined,
  list: undefined,
}

const userReducer = function (state = initialState, action) {
  switch (action.type) {
    case CLEAR_USER:
      return {
        ...state,
        detail: undefined,
      }
    case SET_USER:
      return {
        ...state,
        detail: action.payload.detail,
      }
    case SET_USERS:
      return {
        ...state,
        list: action.payload.list,
      }
    default:
      return state;
  }
}

export default userReducer;
