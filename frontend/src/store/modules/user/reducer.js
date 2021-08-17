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
    case CLEAR_USER: {
      return {
        ...state,
        detail: undefined,
      };
    }
    case SET_USER: {
      const { detail } = action.payload;
      return {
        ...state,
        detail,
      };
    }
    case SET_USERS: {
      const { list } = action.payload;
      return {
        ...state,
        list,
      };
    }
    default: {
      return state;
    }
  }
}

export default userReducer;
