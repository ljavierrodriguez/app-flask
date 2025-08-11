import React from 'react'

const App = () => {
    return (
        <Routes>
            <Route path="/users/:id" element={<UserDetail />} />
            <Route path="/" element={<Home />} />
        </Routes>
    )
}

export default App