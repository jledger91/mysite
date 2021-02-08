import { SET_FILM, SET_FILMS } from './actions';

export const initialState = {
}

const filmReducer = function (state = initialState, action) {
  switch (action.type) {
    case SET_FILM:
      return {
        ...state,
        detail: action.payload.detail,
      }
    case SET_FILMS:
      const { key, list } = action.payload;
      return  {
        ...state,
        list: key === undefined ? {
          ...state.list,
          results: list
        } : {
          ...state.list,
          [key]: list,
        }
      }
    default:
      return state;
  }
}

export default filmReducer;
