import './SearchBar.scss';

import { useState } from 'react';
import { useHistory } from 'react-router';

import InputBase from '@material-ui/core/InputBase';
import SearchIcon from '@material-ui/icons/Search';

import { SEARCH } from '../routes';

const SearchBar = (props) => {
  
  const {
    initialValue,
    onChange: propsHandleChange,
    onKeyPress: propsHandleKeyPress,
  } = props;
  
  const history = useHistory();
  const [value, setValue] = useState(initialValue || '');
  
  const handleChange = (event) => {
    setValue(event.target.value);
  };
  
  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      history.push(`${SEARCH}?query=${value}`);
    }
  };
  
  return (
    <div className='search-bar'>
      <div className='search-icon'>
        <SearchIcon />
      </div>
      <InputBase className='search-input'
                 value={value}
                 onChange={propsHandleChange || handleChange}
                 onKeyPress={propsHandleKeyPress || handleKeyPress}
                 placeholder='Search…'/>
    </div>
  );
}

export default SearchBar;
