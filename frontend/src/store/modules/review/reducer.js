import {
  CLEAR_REVIEW,
  CLEAR_REVIEWS,
  SET_REVIEW,
  SET_REVIEWS,
} from './actions';

export const initialState = {
  detail: undefined,
  list: undefined,
}

const reviewReducer = function (state = initialState, action) {
  switch (action.type) {
    case CLEAR_REVIEW: {
      return {
        ...state,
        detail: undefined,
      };
    }
    case CLEAR_REVIEWS: {
      return {
        ...state,
        list: undefined,
      };
    }
    case SET_REVIEW: {
      const { detail } = action.payload;
      return {
        ...state,
        detail,
      };
    }
    case SET_REVIEWS: {
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

export default reviewReducer;
