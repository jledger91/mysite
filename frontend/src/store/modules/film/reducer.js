import {
  CLEAR_FILM,
  CLEAR_FILMS,
  SET_FILM,
  SET_FILMS,
} from './actions';

export const initialState = {
  detail: undefined,
  list: undefined,
}

const filmReducer = function (state = initialState, action) {
  switch (action.type) {
    case CLEAR_FILM: {
      return {
        ...state,
        detail: undefined,
      };
    }
    case CLEAR_FILMS: {
      const key = action.payload;
      return {
        ...state,
        list: {
          ...state.list,
          [(key === undefined) ? '_' : key]: undefined,
        }
      };
    }
    case SET_FILM: {
      const { detail } = action.payload;
      return {
        ...state,
        detail,
      };
    }
    case SET_FILMS: {
      const { key, list } = action.payload;
      return  {
        ...state,
        list: {
          ...state.list,
          [(key === undefined) ? '_' : key]: list,
        }
      };
    }
    default: {
      return state;
    }
  }
};

export default filmReducer;
